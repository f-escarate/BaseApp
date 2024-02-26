<script>
    import "../app.css";
    import Navbar from "../components/Navbar.svelte";
</script>
<Navbar/>

<div class='mx-auto w-[75%] my-5 h-full p-4 space-y-4'>
    <slot />
</div>  