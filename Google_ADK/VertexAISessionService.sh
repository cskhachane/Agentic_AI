curl -X POST \
     -H "Content-Type: application/json; charset=utf-8" \
     -d {} \
     "https://us-central1-aiplatform.googleapis.com/v1/projects/504822835633/locations/us-central1/reasoningEngines/3225082009034424320/sessions"

     "https://us-central1-aiplatform.googleapis.com/projects/PROJECT_ID/locations/us-central1/reasoningEngines/AGENT_ENGINE_ID/sessions"


      curl.exe -X POST "http://127.0.0.1:8080/apps/google_search_agent/users/cskhachane/sessions" \                                
      -H "Content-Type: application/json" \
      -d '{ "key1":"value1","key2":42}'

      {"id":"daa1f1d6-954f-4770-b4db-3d8479a3ea9d","appName":"google_search_agent","userId":"cskhachane","state":{},"events":[],"lastUpdateTime":1772089382.0445883}

      curl.exe -X GET "http://127.0.0.1:8080/apps/google_search_agent/users/cskhachane/sessions/daa1f1d6-954f-4770-b4db-3d8479a3ea9d" \                                
      -H "Content-Type: application/json"