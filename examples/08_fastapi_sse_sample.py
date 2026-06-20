import time

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, StreamingResponse

app = FastAPI()


def fake_ai_events():
    tokens = ["こんにちは", "。", "SSE", "で", "少しずつ", "表示します", "。"]

    for token in tokens:
        yield f"data: {token}\n\n"
        time.sleep(0.5)


@app.get("/")
def index():
    return HTMLResponse(
        """
        <div id="output"></div>
        <script>
          const output = document.getElementById("output");
          const eventSource = new EventSource("/chat");

          eventSource.onmessage = (event) => {
            output.textContent += event.data;
          };
        </script>
        """
    )


@app.get("/chat")
def chat():
    return StreamingResponse(
        fake_ai_events(),
        media_type="text/event-stream",
    )
