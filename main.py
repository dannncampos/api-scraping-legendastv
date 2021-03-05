"""FastAPI Entrypoint"""
from fastapi import FastAPI, HTTPException
from src.crawlers.legendastv.service.service_legendastv import ServiceLegendasTv


app = FastAPI()

PROCESS = {} # Connect to DB looking for process


@app.get("/process/{process_id}")
async def read_process(process_id: str):
    """Get process from BD

    Args:
        process_id (str): The ID of the searching

    Raises:
        HTTPException: An exception ocurred. Something went wrong!

    Returns:
        dict: The JSON dict with the search details
    """
    if process_id not in PROCESS:
        raise HTTPException(
            status_code=404,
            detail="Process ID not found"
            )
    return {"process": PROCESS[process_id]}


@app.post("/legendastv/term")
async def search_legendas_tv(term: str, user: str, password: str):
    """Legendas TV API

    Args:
        term (str): The term to do the search.
        user (str): Legendas Tv User's Login.
        password (str): Legendas Tv User's Password.

    Returns:
        dict: The JSON dict with the search details
    """
    return ServiceLegendasTv(term, user, password).capture_by_term()
