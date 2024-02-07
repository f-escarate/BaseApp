<script>
    import { Avatar, Dropdown, DropdownHeader, DropdownItem, DropdownDivider, NavHamburger, Button } from 'flowbite-svelte';
    let name = 'John Doe';
    let email = 'john@doe.com';
    let autenticated = true;
    let image = '';
</script>

{#if autenticated}
    <div class="flex items-center md:order-2">
        <Avatar id="avatar-menu" src={image} />
        <NavHamburger class1="w-full md:flex md:w-auto md:order-1" />
    </div>
    <Dropdown placement="bottom" triggeredBy="#avatar-menu">
        <DropdownHeader>
            <span class="block text-sm">{name}</span>
            <span class="block truncate text-sm font-medium">{email}</span>
        </DropdownHeader>
        <DropdownItem>My Entries</DropdownItem>
        <DropdownItem>Account Settings</DropdownItem>
        <DropdownDivider />
        <DropdownItem>Sign out</DropdownItem>
    </Dropdown>
{:else}
    <div class="flex md:order-2">
        <Button size="sm">Login</Button>
    </div>
{/if}