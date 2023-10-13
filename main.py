# main.py
# from deta import Base
from fastapi import FastAPI
from fastapi.responses import FileResponse, HTMLResponse
import subprocess
from pydantic import BaseModel  # pylint: disable=no-name-in-module

app = FastAPI()

@app.get("/", response_class=FileResponse)
async def read_root():
    return FileResponse('./static/index.html')

@app.get("/run-tests", response_class=HTMLResponse)
async def run_tests():
    # test_counter_item = db_config.get("test_counter")
    # db_config.put(str(test_counter_item["value"] + 1), "test_counter")
    
    result = subprocess.run(['behave'], capture_output=True, text=True)
    result_lines = result.stdout.split("\n")
    result_html = "<br>".join(result_lines)
    return result_html

@app.get("/steps-catalog", response_class=HTMLResponse)
async def steps_catalog():
    result = subprocess.run(['behave', '--steps-catalog'], capture_output=True, text=True)
    result_lines = result.stdout.split("\n")
    result_html = "<br>".join(result_lines)
    return result_html