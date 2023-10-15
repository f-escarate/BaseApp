/** @type {import('./$types').Actions} */
export const actions = {
    submit: async ({ request }) => {
        const data = await request.formData();
        console.log(data);
    }
};