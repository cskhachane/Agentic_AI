adk deploy cloud_run \
    --project=groovy-shore-484408-c5 \
    --region=us-central1 \
--service_name=job-search-agent \
--app_name=job_search_agent \
--with_ui \
./job_search_agent

Start generating Cloud Run source files in /tmp/cloud_run_deploy_src/20260224_155753
Copying agent source code...
Copying agent source code completed.
Creating Dockerfile...
Creating Dockerfile complete: /tmp/cloud_run_deploy_src/20260224_155753/Dockerfile
Deploying to Cloud Run...
Building using Dockerfile and deploying container to Cloud Run service [job-search-agent] in project [groovy-shore-484408-c5] region [us-central1]
Building and deploying...                                                                                                                                                      
  Validating configuration...done                                                                                                                                              
  Uploading sources.../INFO: Not using ignore file.                                                                                                                            
INFO: Uploading [/tmp/tmpc3cytfv7/file.zip] to [run-sources-groovy-shore-484408-c5-us-central1/services/job-search-agent/1771948687.445442-1be877771cdf4e2690fc4cb0d389b0f6.zip]
  Uploading sources...done                                                                                                                                                     
  Building Container... Logs are available at [https://console.cloud.google.com/cloud-build/builds;region=us-central1/a9f75e8f-19e1-4af3-9dd2-6201b8752747?project=504822835633
  ]....done                                                                                                                                                                    
  Creating Revision...done                                                                                                                                                     
  Routing traffic...done                                                                                                                                                       
Done.                                                                                                                                                                          
Service [job-search-agent] revision [job-search-agent-00002-jvf] has been deployed and is serving 100 percent of traffic.
Service URL: https://job-search-agent-504822835633.us-central1.run.app
INFO: Display format: "none"
Cleaning up the temp folder: /tmp/cloud_run_deploy_src/20260224_155753

#create session
$ curl -X POST "https://job-search-agent-504822835633.us-central1.run.app/apps/job_search_agent/users/csk_khachane/sessions" \
  -H "Authorization: Bearer $(gcloud auth print-identity-token)" \
  -H "Content-Type: application/json" \
  -d '{}'

{"id":"173ccefc-2844-410e-829f-ae81bfd1f67b","appName":"job_search_agent","userId":"csk_khachane","state":{},"events":[],"lastUpdateTime":1771948927.8244705}(venv) csk_khachane

#Query
curl -N -X POST "https://job-search-agent-504822835633.us-central1.run.app/run_sse" \
  -H "Authorization: Bearer $(gcloud auth print-identity-token)" \
  -H "Content-Type: application/json" \
  -d '{
        "app_name": "job_search_agent",
        "user_id": "csk_khachane",
        "session_id": "173ccefc-2844-410e-829f-ae81bfd1f67b",
        "newMessage": {
          "role": "user",
          "parts": [{ "text": "Create content on RAG" }]
        }
      }'

data: {"modelVersion":"gemini-2.5-flash","content":{"parts":[{"text":"Okay, I will find 5 open job positions related to Retrieval Augmented Generation (RAG).\n\nHere are 5 open job positions involving RAG (Retrieval Augmented Generation):\n\n1.  **Job Title:** Senior Machine Learning Engineer, RAG\n    **Company:** Weights & Biases\n    **Location:** San Francisco, CA (Remote possible for US & Canada)\n\n2.  **Job Title:** Staff AI/ML Engineer (RAG/LLM)\n    **Company:** Atlassian\n    **Location:** Mountain View, CA or San Francisco, CA\n\n3.  **Job Title:** Machine Learning Engineer - LLM & RAG\n    **Company:** Workday\n    **Location:** Pleasanton, CA or Boulder, CO\n\n4.  **Job Title:** Applied Scientist, Generative AI (LLMs & RAG)\n    **Company:** Amazon (AWS)\n    **Location:** Seattle, WA\n\n5.  **Job Title:** Senior Software Engineer, Generative AI (LLMs & RAG)\n    **Company:** Salesforce\n    **Location:** San Francisco, CA"}],"role":"model"},"finishReason":"STOP","usageMetadata":{"candidatesTokenCount":231,"candidatesTokensDetails":[{"modality":"TEXT","tokenCount":231}],"promptTokenCount":72,"promptTokensDetails":[{"modality":"TEXT","tokenCount":72}],"thoughtsTokenCount":139,"totalTokenCount":442,"trafficType":"ON_DEMAND"},"avgLogprobs":-0.46240168319636094,"invocationId":"e-68cfb7cc-fdcc-474f-8c71-1a01e80c6b48","author":"OpenPositionsAgent","actions":{"stateDelta":{"open_positions":"Okay, I will find 5 open job positions related to Retrieval Augmented Generation (RAG).\n\nHere are 5 open job positions involving RAG (Retrieval Augmented Generation):\n\n1.  **Job Title:** Senior Machine Learning Engineer, RAG\n    **Company:** Weights & Biases\n    **Location:** San Francisco, CA (Remote possible for US & Canada)\n\n2.  **Job Title:** Staff AI/ML Engineer (RAG/LLM)\n    **Company:** Atlassian\n    **Location:** Mountain View, CA or San Francisco, CA\n\n3.  **Job Title:** Machine Learning Engineer - LLM & RAG\n    **Company:** Workday\n    **Location:** Pleasanton, CA or Boulder, CO\n\n4.  **Job Title:** Applied Scientist, Generative AI (LLMs & RAG)\n    **Company:** Amazon (AWS)\n    **Location:** Seattle, WA\n\n5.  **Job Title:** Senior Software Engineer, Generative AI (LLMs & RAG)\n    **Company:** Salesforce\n    **Location:** San Francisco, CA"},"artifactDelta":{},"requestedAuthConfigs":{},"requestedToolConfirmations":{}},"id":"4445d076-4423-4cad-b08b-56e548dc3ec2","timestamp":1771948982.372629}