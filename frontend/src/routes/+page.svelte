<script>
    import data from '$lib/home.json';
    const text_style = (idx) => {
        let margins = ['md:mt-[-2%]', 'md:mb-[-2%]'];
        let md_style = `md:w-2/3 lg:w-[60%] xl:w-[52%] md:text-2xl z-10 ${margins[idx%2]}`; 
        let sm_style = 'w-full'
        return `h-full p-5 text-xl bg-sky-500 text-white ${md_style} ${sm_style}`;
    }
    const div_style = (idx) => {
        let paddings = ['pb-[2%]', 'pt-[2%]'];
        return `flex m-10 relative h-full ${paddings[idx%2]}`;
    }
</script>

<main class='flex flex-col h-full relative m-10'>
    {#each data as element, i}
        <div class={div_style(i)}>
            <div class={text_style(i)}>
                {element.text}
            </div>
            <img
                class='max-w-[75%] lg:min-w-[52%] max-h-full right-10 bottom-0 bg-contain absolute invisible md:visible'
                src={element.photo}
                alt={element.photo}
            />
        </div>
    {/each}
</main>