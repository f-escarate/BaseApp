<script>
    import Navbar from '../Navbar.svelte';
    import Form from './Form.svelte';
</script>

<main>
    <Navbar />
    <div class='mx-10 my-5 rounded-xl border-4 border-blue-300 h-full p-4 space-y-4'>
        <h1 class='text-4xl font-bold'>Add Entry</h1>
        <Form />
    </div>
</main>

<style lang="postcss">
    :global(html) {
        background-color: theme(colors.gray.100);
    }
</style>