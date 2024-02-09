<script>
    import { Navbar, NavBrand, NavLi, NavUl } from 'flowbite-svelte';
    import Cookies from 'js-cookie';
    let token = Cookies.get('token');
    var nonActiveClass = 'text-xl md:transition-all md:hover:text-blue-400 md:hover:scale-125'
    var activeClass = nonActiveClass+' md:border-blue-400 md:border-b-2 md:rounded-none'

    import { page } from '$app/stores';
    import UserButton from './UserButton.svelte';
    $: activeUrl = $page.url.pathname;
</script>

<Navbar class="md:px-10">
    <NavBrand href="/">
        <img src='/favicon.png' class="me-3 h-6 sm:h-9" alt="Logo" />
        <span class="self-center whitespace-nowrap text-2xl font-semibold dark:text-white">Base App</span>
    </NavBrand>
    <UserButton/>
    <NavUl {activeUrl} {activeClass} {nonActiveClass}>
        <NavLi href="/">Home</NavLi>
        {#if token}
            <NavLi href="/add/">Add Entry</NavLi>
        {/if}
        <NavLi href="/searchEntries/">Search Entries</NavLi>
        <NavLi href="/aboutUs/">About us</NavLi>
    </NavUl>
</Navbar>