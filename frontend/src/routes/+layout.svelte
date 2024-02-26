<script>
    import "../app.css";
    import Footer from "../components/Footer.svelte";
    import Navbar from "../components/Navbar.svelte";
</script>

<div class='min-h-screen flex flex-col justify-between'>
    <Navbar/>
    <div class='mx-auto w-[75%] my-5 h-full p-4 space-y-4'>
        <slot />
    </div>  
    <Footer/>
</div>