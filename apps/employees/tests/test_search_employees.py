import pytest
from apps.employees.models import Employee
from apps.employees.enums import Location, Status, Department

@pytest.mark.asyncio
async def test_empty(client):
    response = await client.get("/v1/employee/search")
    assert response.status_code == 200
    assert response.json() == []

@pytest.mark.asyncio
async def test_filter(client, async_session):
    emp = Employee(
        firstname="A",
        lastname="B",
        department=Department.hr,
        position="Dev",
        location=Location.ind,
        status=Status.active
    )
    async_session.add(emp)
    await async_session.commit()

    response = await client.get("/v1/employee/search", params={"department":"hr"})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list) and len(data) == 1
    assert data[0]["firstname"] == "A"
