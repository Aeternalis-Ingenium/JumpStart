import json

from pytest import mark


@mark.anyio
async def test_api_health_check_healthy(async_client):
    response = await async_client.get("/api/")
    assert response.status_code == 200
    assert json.loads(response.content) == {"status": "💚"}
