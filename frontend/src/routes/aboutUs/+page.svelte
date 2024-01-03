<script>
    import data from "$lib/aboutUs.json"
    const styles = [
        "animate-delay-100 bg-sky-500",
        "animate-delay-300 bg-yellow-400",
        "animate-delay-500 bg-green-500"
    ];
    const card_style = 'w-full min-h-full p-10 text-white animate-fade-down animate-ease-out animate-duration-300';
</script>

<main>
    <div class='flex mx-20 my-5 gap-4'>
        {#each data as element, i}
            <div class={card_style.concat(" ", styles[i])}>
                <h1 class='text-4xl font-bold mb-8'>{element.name}</h1>
                {#each Object.entries(element.sections) as [title, text]}
                    <div class='my-3'>
                        <p class='font-bold text-lg'>{title}</p>
                        <p>{text}</p>
                    </div>
                {/each}
            </div>
        {/each}
    </div>
</main>