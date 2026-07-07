from fastapi import APIRouter

from yorha.kernel.runtime import runtime

router = APIRouter(prefix="/tools", tags=["Tools"])

from yorha.api.models import ToolDefinition



@router.get("")
async def list_tools():
    definitions = []

    for tool in runtime.registry.list_tools():
        definitions.append(
            ToolDefinition(
                name=tool.manifest.name,
                description=tool.manifest.description,
                input_schema=tool.input_model.model_json_schema(),
            )
        )

    return definitions


@router.post("/{tool_name}")
async def execute_tool(
    tool_name: str,
    arguments: dict[str, Any],
):
    try:
        tool = runtime.registry.get_tool(tool_name)
    except KeyError:
        raise HTTPException(
            status_code=404,
            detail=f"Unknown tool '{tool_name}'.",
        )

    result = await tool.execute(**arguments)

    return result.model_dump(mode="json")

