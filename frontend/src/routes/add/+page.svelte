<script>
    import Form from './Form.svelte';
    import Cookies from 'js-cookie';
    import { onMount } from 'svelte';
    let token;
    onMount(() => {
        token = Cookies.get('token');
        if (token===undefined) {
            if(!alert("You have to be logged in to access this page")) {
                window.location.href = "/login";
            }
        }
    });
</script>

{#if token}
    <div class='mx-auto w-[75%] my-5 h-full p-4 space-y-4'>
        <h1 class='text-4xl font-bold'>Add Entry</h1>
        <Form token={token}/>
    </div>
{/if}