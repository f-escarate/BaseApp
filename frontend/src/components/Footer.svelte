<script>
    import { Footer, FooterCopyright, FooterBrand } from 'flowbite-svelte';
</script>
  
<Footer footerType="logo">
    <div class="sm:flex sm:items-center sm:justify-between">
        <FooterBrand href="/" src="/favicon.png" alt="Base App Logo" name="Base App" />
    </div>
    <hr class="my-6 border-gray-200 sm:mx-auto dark:border-gray-700 lg:my-8" />
    <FooterCopyright href="/" by="Base App" />
</Footer>