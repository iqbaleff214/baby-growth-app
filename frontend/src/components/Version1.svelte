<script>
    import Spinner from "./c/Spinner.svelte";

    let loading = false;
    
    let fatherPhoto;
    let motherPhoto;
    
    let result;
    
    const formData = new FormData();

    const submit = () => {
        loading = true;
        if (!fatherPhoto || !motherPhoto) {
            loading = false;
            console.log('FAILED');
            return;
        }

        formData.append('father', fatherPhoto[0]);
        formData.append('mother', motherPhoto[0]);

        // Send POST request with file
        fetch('http://127.0.0.1:8000/v1/process-image', {
            method: 'POST',
            body: formData,
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                
                // Check the content type to determine how to handle the response
                const contentType = response.headers.get('Content-Type');
                console.log('type:', contentType);
                
                if (contentType && contentType.includes('image')) {
                    return response.blob(); // If it's an image, process as blob
                } else if (contentType && contentType.includes('application/json')) {
                    return response.json(); // If it's JSON, parse as JSON
                } else {
                    throw new Error('Unsupported content type');
                }
            })
            .then(data => {
                const image = URL.createObjectURL(data);
                result = image;
            })
            .catch(error => console.error('Error uploading file:', error))
            .finally(() => {
                loading = false;
            });
    };
</script>

<div class="max-w-96 mx-auto bg-white rounded-lg shadow p-5 flex flex-col gap-y-6">
    <div class="flex flex-col gap-y-3">
      <div class="flex flex-col gap-y-2">
        <label for="father">Father Picture</label>
        <input type="file" id="father" accept="image/*" bind:files={fatherPhoto}>
        {#if fatherPhoto}
            <div>
                <img src={URL.createObjectURL(fatherPhoto[0])} alt="result" class="rounded" />
            </div>
        {/if}
      </div>
      <div class="flex flex-col gap-y-2">
        <label for="mother">Mother Picture</label>
        <input type="file" id="mother" accept="image/*" bind:files={motherPhoto}>
        {#if motherPhoto}
            <div>
                <img src={URL.createObjectURL(motherPhoto[0])} alt="result" class="rounded" />
            </div>
        {/if}
      </div>
    </div>
    <div>
        {#if result}
            <h3 class="mb-2">Baby</h3>
            <img src={result} alt="result" class="mb-3 rounded" />
        {/if}

      <button 
        type="button" disabled={loading || !fatherPhoto || !motherPhoto} on:click={submit}
        class="flex items-center gap-x-2 px-4 py-2 bg-blue-500 text-white font-semibold rounded-lg shadow-md disabled:cursor-not-allowed focus:outline-none focus:ring-2 focus:ring-blue-300">
        Proceed
        {#if loading}
            <Spinner />
        {/if}
      </button>

      <p class="text-xs text-center text-gray-400 mt-5">v1</p>
    </div>
</div>