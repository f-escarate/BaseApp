<script>
    import { FloatingLabelInput, Textarea, Range, Label, Button } from 'flowbite-svelte';
    import { onMount } from 'svelte';
    import { HOST } from '$lib/constants';

    export let token;
    export let http_method = 'POST';
    export let endpoint_url = '/post_item/';
    export let entry = {
        title : '',
        description : '',
        continuousVar : 5.0,
        discreteVar : 5,
        date : null,
        image : null,
    };
    export const previewImage = () => {
        console.log(entry.image);
        var preview = document.getElementById('preview');
        preview.src = URL.createObjectURL(entry.image);
        preview.onload = () => {
            URL.revokeObjectURL(preview.src) // free memory
        }
    }

    const restartForm = () => {
        entry.title = '';
        entry.description = '';
        entry.continuousVar = 5.0;
        entry.discreteVar = 5;
        entry.date = null;
        entry.image = null;
        var preview = document.getElementById('preview');
        preview.src = '';
    }

    const validation = () => {
        let msg = '';
        if (entry.title == '')
            msg += 'Title cannot be empty\n';
        if (entry.description == '')
            msg += 'Description cannot be empty\n';
        if (entry.date == null)
            msg +=  'Date cannot be empty\n';
        if (entry.image == null)
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
        for ( var key in entry ) {
            data.append(key, entry[key]);
        }
        const response = await fetch(`${HOST}${endpoint_url}`, {
            method: http_method,
            headers: {
                Authorization: `Bearer ${token}`
            },
            body: data
        });
        const json = await response.json();
        if (json.status == 'success') {
            alert('Successfully added');
            restartForm();
        } else {
            alert('Failed to add');
        }
    }
    const loadFile = (event) => {
        entry.image = event.target.files[0];
        previewImage();
    };

</script>
<div class='border-4 border-blue-300 p-5'>
    <div class='grid gap-6 items-end w-full md:grid-cols-2'>
        <div class='md:col-span-2'>
            <Label for="title" class="mb-2">Title</Label>
            <FloatingLabelInput style="filled" name="title" id="title" type="text" label="Title" bind:value={entry.title}/>
        </div>
        <div class='md:col-span-1 h-full flex flex-col justify-between'>
            <div class="mb-4">
                <Label for="continuous-var">Continuous variable</Label>
                <Range id="continuous-var" name="continuous-var" min="0" max="10" step="0.001" bind:value={entry.continuousVar}/>
                <p class='text-xs italic'>Value: {entry.continuousVar}</p>
            </div>

            <div class="mb-4">
                <Label for="discrete-var">Discrete variable</Label>
                <Range id="discrete-var" name="discrete-var" min="0" max="10" step="1" bind:value={entry.discreteVar}/>
                <p class='text-xs italic'>Value: {entry.discreteVar}</p>
            </div>

            <div class="flex flex-col">
                <Label for="date" class="mb-1">Date</Label>
                <input type="date" id="date" name="date" class="p-2" bind:value={entry.date}>
            </div>
        </div>

        <div class="h-full">
            <Label for="description" class="mb-2">Description</Label>
            <Textarea class="h-full" id="description" placeholder="Enter description" rows="5" name="description" bind:value={entry.description}/>
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
</div>