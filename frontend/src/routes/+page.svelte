<script>
    import { onMount } from 'svelte';
    import data from '$lib/home.json';

    const text_style = (idx) => {
        let margins = ['md:mt-[-2%]', 'md:mb-[-2%]'];
        let md_style = `md:w-2/3 lg:w-[60%] xl:w-[52%] md:text-2xl z-10 ${margins[idx%2]}`; 
        let sm_style = 'w-full'
        return `h-full p-5 text-xl bg-sky-500 text-white ${md_style} ${sm_style}`;
    }
    const div_style = (idx) => {
        let paddings = ['pb-[2%]', 'pt-[2%]'];
        return `animated-div opacity-0 flex m-10 relative h-full ${paddings[idx%2]}`;
    }

    onMount(() => {
        const targets = document.querySelectorAll('.animated-div');
        const options = {
            root: null, // use the viewport as the root
            rootMargin: '0px',
            threshold: 0.5, // change this value as needed, 0.5 means when 50% of the element is visible
        };

        for (let i = 0; i < targets.length; i++){
            let target = targets[i];
            const observer = new IntersectionObserver((entries) => {
                entries.forEach((entry) => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('animate-fade-right');
                        entry.target.classList.add('animate-duration-500');
                        entry.target.classList.add('animate-ease-out');
                        observer.unobserve(entry.target);
                    }
                });
            }, options);

            if (target) 
                observer.observe(target);
        }
    });
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