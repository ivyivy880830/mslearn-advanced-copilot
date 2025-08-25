## 如何執行本專案

1. 安裝依賴套件  
   在專案根目錄下執行：
   ```sh
   pip install -r requirements.txt
   ```

2. 啟動 FastAPI 伺服器  
   在專案根目錄下執行：
   ```sh
   uvicorn main:app --reload
   ```
   預設會在 http://localhost:8000 運行。

3. 開啟 API 文件  
   在瀏覽器中前往 [http://localhost:8000/docs](http://localhost:8000/docs) 查看 API Swagger 文件。

4. 執行測試  
   在專案根目錄下執行：
   ```sh
   pytest
   ```
   會自動執行 test_main.py 內的所有測試案例。

---

如需在 Docker 或 Codespaces 環境下執行，請參考 devcontainer.json 及 .devcontainer/Dockerfile 設定。
