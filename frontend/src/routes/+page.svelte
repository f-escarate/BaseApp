<script>
    import Navbar from './Navbar.svelte';
</script>

<main>
    <Navbar />
    <div class='p-4 mx-10 my-5 rounded-xl border-4 border-blue-300'>
        <h1 class='text-4xl font-bold'>Page</h1>
    </div>
</main>

<style lang="postcss">
    :global(html) {
        background-color: theme(colors.gray.100);
    }
</style>