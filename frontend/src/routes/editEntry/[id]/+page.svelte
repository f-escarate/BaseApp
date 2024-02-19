<script>
    import Form from '../../../components/Form.svelte';
    import Cookies from 'js-cookie';
    import { HOST } from '$lib/constants';
    import { onMount } from 'svelte';

    /** @type {import('./$types').PageData} */
	export let data;
    let id = data.id
    let token = null;
    let entry = {
        title: '',
        description: '',
        continuousVar: 5.0,
        discreteVar: 5,
        date: null,
        image: null
    };
    let form;
    onMount(async () => {
        token = Cookies.get('token');
        if (token===undefined) {
            if(!alert("You have to be logged in to access this page")) {
                window.location.href = "/login";
            }
        }
        const response = await fetch(`${HOST}/get_item/${id}/`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
            }
        });
        const json = await response.json();
        entry = json;
        let extension = entry.image;
        const img_response = await fetch(`${HOST}/get_image/${entry.id}`, {
            method: 'GET',
            headers: {
                'Content-Type': `image/${entry.image}`
            }
        });
        entry.image = new File([await img_response.blob()], `image.${extension}`);
        form.previewImage();
    });

</script>

<Form bind:this={form} token={token} entry={entry} endpoint_url={`/update_item/${id}/`} http_method='PATCH'/>