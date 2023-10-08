<script>
    var fruits = ['aa' , 'ab']
    var valueStandard = ''
</script>
<main>
    <div class='rounded-l border-4 border-blue-300 p-5'>
        <form method='POST' action='?/add' class='grid justify-items-center'>
            <label class='w-full mb-4'>
                Entry title
                <input type="text" name="title" id="title" placeholder="Title"
                    class='w-full p-2 border-2 border-blue-400 rounded-md'>
            </label>        
            <button class='w-1/3 mx-auto my-4 px-4 py-2 rounded bg-blue-400' >Add</button>
        </form>
    </div>
</main>