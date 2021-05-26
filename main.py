import uvicorn
#fdsaf
if __name__ == "__main__":
    uvicorn.run("src.app:app", host="0.0.0.0", port=8000, reload=True, debug=True)
