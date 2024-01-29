<script>
    import { FloatingLabelInput, Textarea, Range, Label, Button } from 'flowbite-svelte';
    const HOST = 'http://localhost:8000';
    let title = '';
    let description = '';
    let continuousVar = 5.0;
    let discreteVar = 5;
    let date = null;
    let image = null;
    
    const validation = () => {
        let msg = '';
        if (title == '')
            msg += 'Title cannot be empty\n';
        if (description == '')
            msg += 'Description cannot be empty\n';
        if (date == null)
            msg +=  'Date cannot be empty\n';
        if (image == null)
            msg += 'Image cannot be empty\n';
        
        if (msg !== '') {
            alert(msg);
            return false;
        }
        return true;
    }
    
    const handleSubmit = async (e) => {
        if (!validation()) {
            return;
        }
		const data = new FormData();
        data.append('title', title);
        data.append('description', description);
        data.append('continuousVar', continuousVar);
        data.append('discreteVar', discreteVar);
        data.append('date', date);
        data.append('image', image);

        const response = await fetch(`${HOST}/post_item/`, {
            method: "POST",
            body: data
        });
        const json = await response.json();
        console.log(json);
    }

    const loadFile = (event) => {
        var preview = document.getElementById('preview');
        image = event.target.files[0];
        preview.src = URL.createObjectURL(image);
        preview.onload = () => {
            URL.revokeObjectURL(preview.src) // free memory
        }
    };

</script>
<main class='border-4 border-blue-300 p-5'>
    <div class='grid gap-6 items-end w-full md:grid-cols-2'>
        <div class='md:col-span-2'>
            <Label for="title" class="mb-2">Title</Label>
            <FloatingLabelInput style="filled" name="title" id="title" type="text" label="Title" bind:value={title}/>
        </div>
        <div class='md:col-span-1 h-full flex flex-col justify-between'>
            <div class="mb-4">
                <Label for="continuous-var">Continuous variable</Label>
                <Range id="continuous-var" name="continuous-var" min="0" max="10" step="0.001" bind:value={continuousVar}/>
                <p class='text-xs italic'>Value: {continuousVar}</p>
            </div>

            <div class="mb-4">
                <Label for="discrete-var">Discrete variable</Label>
                <Range id="discrete-var" name="discrete-var" min="0" max="10" step="1" bind:value={discreteVar}/>
                <p class='text-xs italic'>Value: {discreteVar}</p>
            </div>

            <div class="flex flex-col">
                <Label for="date" class="mb-1">Date</Label>
                <input type="date" id="date" name="date" class="p-2" bind:value={date}>
            </div>
        </div>

        <div class="h-full">
            <Label for="description" class="mb-2">Description</Label>
            <Textarea class="h-full" id="description" placeholder="Enter description" rows="5" name="description" bind:value={description}/>
        </div>

        <div class="my-2 flex-row align-center">
            <Label for="image" class="mb-2">
            Upload image
            <div class="my-4 p-1 flex bg-blue-300 hover:bg-blue-500 text-center hover:text-white transition-colors duration-400 ease-in-out">
                <img id="preview" class="md:w-1/2 m-auto p-2" alt="Data">
                <input type="file" id="image" name="image" class="w-0 invisible" on:change={loadFile}>
            </div>
            </Label>
        </div>
        <Button class='md:col-span-2 w-[50%] mx-auto h-full' color="green" on:click={handleSubmit} pill>Add</Button>
    </div>
</main>