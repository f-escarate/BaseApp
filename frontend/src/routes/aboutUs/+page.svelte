<script>
    import data from '$lib/aboutUs.json';
    let card_style = 'w-full min-h-full p-10 text-white'
    let keys = Object.keys(data)
</script>

<main>
    <div class='flex mx-20 my-5 gap-4'>
        {#each keys as key}
            <div class={`${card_style} ${data[key].color}`}>
                <h1 class='text-4xl font-bold mb-8'>{key}</h1>
                {#each Object.entries(data[key].sections) as [title, text]}
                    <div class='my-3'>
                        <p class='font-bold text-lg'>{title}</p>
                        <p>{text}</p>
                    </div>
                {/each}
            </div>
        {/each}
    </div>
</main>