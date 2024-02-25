<script>
    import { Avatar, Dropdown, DropdownHeader, DropdownItem, DropdownDivider, NavHamburger, Button } from 'flowbite-svelte';
    import UserIcon from './icons/UserIcon.svelte';
    import Cookies from 'js-cookie';
    import { onMount } from 'svelte';
    import { HOST } from '$lib/constants';
    export let authenticated;

    let data = {
        name: '',
        email: '',
        image: '',
    };
    onMount(async () => {
        if(Cookies.get('token') === undefined) return;
        const response = 
            await fetch(`${HOST}/me/`, {
                method: "GET",
                headers: {
                    accept: "application/json",
                    Authorization: `Bearer ${Cookies.get('token')}`
                }
            });
        const json = await response.json();
        if (json.status == 'success') {
            data.name = json.username;
            data.email = json.email;
            data.image = '';
            authenticated = true;
        } else {
            authenticated = false;
            Cookies.remove('token');
        }
    });
    const handleLogOut = () => {
        Cookies.remove('token');
        data.authenticated = false;
        window.location.href = '/';
    }

</script>

{#if authenticated}
    <div class="flex items-center md:order-2">
        <Avatar id="avatar-menu" src={data.image} />
        <NavHamburger class1="w-full md:flex md:w-auto md:order-1" />
    </div>
    <Dropdown placement="bottom" triggeredBy="#avatar-menu">
        <DropdownHeader>
            <span class="block text-sm">{data.name}</span>
            <span class="block truncate text-sm font-medium">{data.email}</span>
        </DropdownHeader>
        <DropdownItem href='/myEntries/'>My Entries</DropdownItem>
        <DropdownItem>Account Settings</DropdownItem>
        <DropdownDivider />
        <DropdownItem on:click={handleLogOut}>Log out</DropdownItem>
    </Dropdown>
{:else}
    <div class="flex md:order-2 gap-2">
        <Button size="sm" href="/login">
            <UserIcon sx='m-0 text-white'/>
            Log In
        </Button>
    </div>
{/if}