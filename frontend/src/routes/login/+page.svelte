<script>
    import { Tabs, TabItem, FloatingLabelInput , Button} from 'flowbite-svelte';
    import Cookies from 'js-cookie';
    import { HOST } from '$lib/constants';
    let name = '';
    let email = '';
    let pass = '';
    let pass2 = '';

    const handleLogin = async () => {
        const data = new FormData();
        data.append('username', email);
        data.append('password', pass);
        const response = await fetch(`${HOST}/token`, {
            method: "POST",
            body: data
        });
        const json = await response.json();
        if (json.status == 'success') {
            Cookies.set('token', json.access_token, { sameSite:'strict' });
            alert('Successfully logged in');
            window.location.href = '/';
            return;
        }
        alert('Username or password incorrect');
    }

    const handleRegister = async () => {
        if (pass != pass2) {
            alert('Passwords do not match');
            return;
        }
        const data = new FormData();
        data.append('username', name);
        data.append('email', email);
        data.append('password', pass);
        data.append('password2', pass2);
        const response = await fetch(`${HOST}/register/`, {
            method: "POST",
            body: data
        });
        const json = await response.json();
        if (json.status == 'success') {
            alert('Successfully registered');
            window.location.href = '/login';
        }
        else if (json.status == 'error') {
            alert(json.msg);
        }
    }
    const onEnter = (e, func) => {
        if (e.key == 'Enter') {
            func();
        }
    }


</script>

<div class='mx-auto max-w-[50%] my-5 h-full p-4 space-y-4'>
    <Tabs style="underline">
        <TabItem open>
            <span slot="title">Log In</span>
            <div class='flex flex-col gap-4'>
                <FloatingLabelInput style="filled" bind:value={email} on:keydown={(e)=>onEnter(e, handleLogin)} name="email" id="email" type="text" label="Email"/>
                <FloatingLabelInput style="filled" bind:value={pass}  on:keydown={(e)=>onEnter(e, handleLogin)} name="password" id="password" type="password" label="Password"/>
                <Button size="sm" on:click={handleLogin}>Log In</Button>
            </div>
        </TabItem>
        <TabItem>
            <span slot="title">Register</span>
            <div class='flex flex-col gap-4'>
                <FloatingLabelInput bind:value={name}  on:keydown={(e)=>onEnter(e, handleRegister)} style="filled" name="name" id="name" type="text" label="Name"/>
                <FloatingLabelInput bind:value={email} on:keydown={(e)=>onEnter(e, handleRegister)} style="filled" name="email" id="register_email" type="text" label="Email"/>
                <FloatingLabelInput bind:value={pass}  on:keydown={(e)=>onEnter(e, handleRegister)} style="filled" name="password" id="register_password" type="password" label="Password"/>
                <FloatingLabelInput bind:value={pass2} on:keydown={(e)=>onEnter(e, handleRegister)} style="filled" name="password2" id="register_password2" type="password" label="Repeat your password"/>
                <Button size="sm" on:click={handleRegister}>Register</Button>
            </div>
        </TabItem>
    </Tabs>    
</div>
  