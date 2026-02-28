https://googleapis.github.io/genai-toolbox/getting-started/introduction/

(venv) PS C:\Users\c.sunil.khachane\Downloads\IMP_Training\Google_ADK> $VERSION = "0.26.0"
>> curl.exe -o toolbox.exe "https://storage.googleapis.com/genai-toolbox/v$VERSION/windows/amd64/toolbox.exe"
  % Total    % Received % Xferd  Average Speed  Time    Time    Time   Current
                                 Dload  Upload  Total   Spent   Left   Speed
100 258.3M 100 258.3M   0      0  8.42M      0   00:30   00:30          9.73M
(venv) PS C:\Users\c.sunil.khachane\Downloads\IMP_Training\Google_ADK> 


(venv) PS C:\Users\c.sunil.khachane\Downloads\IMP_Training\Google_ADK> .\mcp_toolbox\toolbox --version
toolbox version 0.26.0+binary.windows.amd64.86bf7bf


.\toolbox --tools-file "tools.yaml" --ui

outside venv in terminal
C:\Users\c.sunil.khachane\Downloads\IMP_Training\Google_ADK>npx @modelcontextprotocol/inspector

Need to install the following packages:
@modelcontextprotocol/inspector@0.21.1
Ok to proceed? (y) y
npm warn deprecated inflight@1.0.6: This module is not supported, and leaks memory. Do not use it. Check out lru-cache if you want a good and tested way to coalesce async requests by a key value, which is much more comprehensive and powerful.
npm warn deprecated glob@7.2.3: Old versions of glob are not supported, and contain widely publicized security vulnerabilities, which have been fixed in the current version. Please update. Support for old versions may be purchased (at exorbitant rates) by contacting i@izs.me       
npm warn deprecated node-domexception@1.0.0: Use your platform's native DOMException instead
Starting MCP inspector...
⚙️ Proxy server listening on localhost:6277
🔑 Session token: ddeaa564ac1d1351ad2c93dc2536edcbdfc9b3dd9731310dafb9e670a22dc53b
   Use this token to authenticate requests or set DANGEROUSLY_OMIT_AUTH=true to disable auth

🚀 MCP Inspector is up and running at:
   http://localhost:6274/?MCP_PROXY_AUTH_TOKEN=ddeaa564ac1d1351ad2c93dc2536edcbdfc9b3dd9731310dafb9e670a22dc53b

🌐 Opening browser...
