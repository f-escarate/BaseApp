<script>
    export let entry_data;
    const getImg = async () => {
        const response = await fetch(`http://localhost:8000/get_image/${entry_data.id}/`, {
            method: 'GET',
            headers: {
                'Content-Type': `image/${entry_data.image}`
            }
        });
        return response.blob();
    }
</script>
<div class='m-4 p-8 bg-blue-300'>
    <h1 class='text-4xl'>{entry_data.title}</h1>
    {#await getImg()}
        <h1 class='text-4xl'>Loading</h1>
    {:then image} 
        <div class='flex justify-between'>
            <div>
                <p>{entry_data.description}</p>
                <p class="text-xs font-bold">Fecha {entry_data.date}</p>
            </div>
            <div>
                <img src={URL.createObjectURL(image)} alt={entry_data.id} />
            </div>
        </div>
    {/await}
</div>