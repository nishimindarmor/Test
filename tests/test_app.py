import pytest
from httpx import AsyncClient

from app.main import app


@pytest.mark.asyncio
async def test_health_ok():
    async with AsyncClient(app=app, base_url="http://test") as client:
        resp = await client.get("/api/health")
        assert resp.status_code == 200
        assert resp.json() == {"status": "ok"}


@pytest.mark.asyncio
async def test_echo_roundtrip():
    async with AsyncClient(app=app, base_url="http://test") as client:
        payload = {"message": "hello"}
        resp = await client.post("/api/echo", json=payload)
        assert resp.status_code == 200
        assert resp.json() == {"echo": "hello"}


@pytest.mark.asyncio
async def test_index_renders_html():
    async with AsyncClient(app=app, base_url="http://test") as client:
        resp = await client.get("/")
        assert resp.status_code == 200
        assert "text/html" in resp.headers["content-type"]
        assert "FastAPI Test App" in resp.text