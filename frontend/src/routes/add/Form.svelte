<script>
    export var autocomplete_values = ['val1' , 'val2', 'val3']
    var valueStandard = ''
    import Autocomplete from '@smui-extra/autocomplete'

    function handleSubmit(e) {
		const ACTION_URL = e.target.action
		// get the form fields data and convert it to URLSearchParams
		const formData = new FormData(e.target)
		const data = new URLSearchParams()
		for (let field of formData) {
			const [key, value] = field
			data.append(key, value)
		}
		data.append('autocomplete', valueStandard)


		// check the form's method and send the fetch accordingly
		if (e.target.method.toLowerCase() == 'get') return
		else {
			fetch(ACTION_URL, {
				method: 'POST',
				body: data
			})			
		}
    }


</script>
<main>
    <div class='rounded-l border-4 border-blue-300 p-5'>
        <form method='POST' action='?/add' class='grid justify-items-center' on:submit|preventDefault={handleSubmit}>
            <label class='w-full mb-4'>
                Entry title
                <input type="text" name="title" id="title" placeholder="Title"
                    class='w-full p-2 border-2 border-blue-400 rounded-md'>
            </label>        
            <Autocomplete
				class="w-full"
				id="autocomplete"
				options={autocomplete_values}
				bind:value={valueStandard}
				label="Autocomplete"
				sx={{
					'& .mdc-text-field': {
						width: '100%',
						display: 'flex',
						'&:focus': {
							borderColor: 'blue',
							width: '100%'
						}
					},
				}}
            />
            <button class='w-1/3 mx-auto my-4 px-4 py-2 rounded bg-blue-400' >Add</button>
        </form>
    </div>
</main>