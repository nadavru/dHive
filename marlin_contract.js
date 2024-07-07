const user = {
    'public_key': '9a8cb98fa9a913ede98ccf4468b0262f80c3131eb6d4d9d1d478b9bb94ee48d80073fb8a2ce92d059a6ac797264cbbd54790849dd41b1e3d3f599654d8fe4ce9',
    'id': 'user:9a8cb98fa9a913ede98ccf4468b0262f80c3131eb6d4d9d1d478b9bb94ee48d80073fb8a2ce92d059a6ac797264cbbd54790849dd41b1e3d3f599654d8fe4ce9'
}

const NODE_URL = "http://node1.naptha.ai:7001";

//addEventListener('fetch', event => {
//    event.respondWith(handle(event.request));
//});

async function handle(request) {
    try {
        //const data = await request.json();
        const data = {"module_name":"multiplayer_chat","module_params": {'prompt': 'I would like to count up to ten, one number at a time, stop when you reach ten. Ill start. one.'}};

        const task_data = {
            ...data,
            "consumer_id": user.id,
            "worker_nodes": ["http://node.naptha.ai:7001", "http://node1.naptha.ai:7001"]
        };

        const response = await fetch(`${NODE_URL}/CreateTask`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(task_data)
        });

        if(!response.ok) {
            throw new Error(`Error creating the task`);
        }

        const task_details = await response.json();

        let final_response = "Error while checking task";

        let task_completed = false;

        while(!task_completed) {
            const response = await fetch(`${NODE_URL}/CheckTask`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(task_details)
            });
            
            const task_status = await response.json();

            if(task_status.status == "completed") {
                final_response = JSON.stringify(task_status.results);
                break;
            }

            if(task_status.status == "error") {
                final_response = "Error while executing task";
                break;
            }

            await sleep(3000);
        }
        console.log(final_response)

        return new Response(final_response);

    } catch(err) {
        console.log(err);
        return new Response('Please provide a valid JSON input');
    }
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}
handle()