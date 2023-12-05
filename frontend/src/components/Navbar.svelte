<script>
    import { Navbar, NavBrand, NavLi, NavUl, NavHamburger } from 'flowbite-svelte';
    var nonActiveClass = 'text-xl md:transition-all md:hover:text-blue-400 md:hover:scale-125'
    var activeClass = nonActiveClass+' md:border-blue-400 md:border-b-2 md:rounded-none'

    import { page } from '$app/stores';
    $: activeUrl = $page.url.pathname;
</script>

<main>
    <Navbar class="md:px-10">
        <NavBrand href="/">
            <img src='/favicon.png' class="me-3 h-6 sm:h-9" alt="Logo" />
            <span class="self-center whitespace-nowrap text-2xl font-semibold dark:text-white">Base App</span>
        </NavBrand>
        <NavHamburger/>
        <NavUl {activeUrl} {activeClass} {nonActiveClass}>
            <NavLi href="/">Home</NavLi>
            <NavLi href="/add">Add Entry</NavLi>
        </NavUl>
    </Navbar>
</main>