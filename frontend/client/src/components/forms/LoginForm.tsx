import { useForm } from "react-hook-form"
import AxiosRequest from "../../utils/AxiosRequest"
import type LoginCreadentials from "../../interfeces/LoginCredentials"


const LoginForm = ({onSuccess}: {onSuccess: () => void}) => {

    const { register, handleSubmit } = useForm<LoginCreadentials>()

    const loginUser = async (data: LoginCreadentials) => {
        try {
            const response = await AxiosRequest.post('/token', {
                username: data.username,
                password: data.password
            }, {
                headers: {
                    'Content-Type':'multipart/form-data'
                }
            })
            console.log('Вход успешный', response)
            if (response){
                onSuccess()
            }
        } catch (e) {
            console.error(e)
        }
    }


    return (
        <>
            <form onSubmit={handleSubmit(loginUser)}>
                <input type="text" {...register('username')} />
                <input type="password" {...register('password')} />
                <button type='submit'>логин</button>
            </form>
        </>
    )
}

export default LoginForm