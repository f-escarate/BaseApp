<script>
    import { FloatingLabelInput, Textarea, Range, Label, Button } from 'flowbite-svelte';

    let title = '';
    let description = '';
    let continuousVar = 5;
    let discreteVar = 5;
    
    
    const handleSubmit = async (e) => {
        console.log('Form submitted');
		const data = new URLSearchParams();
		data.append('title', title);
        data.append('description', description);
        data.append('continuousVar', continuousVar);
        data.append('discreteVar', discreteVar);
        const response = await fetch(`${window.location.href}?/submit`, {
            method: "POST",
            body: data
        });
        const json = await response.json();
        console.log(json);
    }

</script>
<main>
    <div class='rounded-xl border-4 border-blue-300 p-5'>
        <div class='grid gap-6 items-end w-full md:grid-cols-2'>
            <div class='md:col-span-2'>
                <Label for="title" class="mb-2">Title</Label>
                <FloatingLabelInput style="filled" name="title" id="title" type="text" label="Title" bind:value={title}/>
            </div>
            <div class='md:col-span-1 h-full'>
                <Label for="continuous-var">Continuous variable</Label>
                <Range id="continuous-var" name="continuous-var" min="0" max="10" step="0.001" bind:value={continuousVar}/>
                <p class='text-xs'>Value: {continuousVar}</p>

                <Label for="discrete-var">Discrete variable</Label>
                <Range id="discrete-var" name="discrete-var" min="0" max="10" step="1" bind:value={discreteVar}/>
                <p class='text-xs'>Value: {discreteVar}</p>
            </div>

            <div>
                <Label for="description" class="mb-2">Description</Label>
                <Textarea id="description" placeholder="Enter description" rows="5" name="description" bind:value={description}/>
            </div>
            <Button class='md:col-span-2 w-[50%] mx-auto' color="green" on:click={handleSubmit} pill>Add</Button>
        </div>
    </div>
</main>