import {useForm} from 'react-hook-form'
import type LoginCreadentials  from '../interfeces/LoginCredentials'
import AxiosRequest from '../utils/AxiosRequest'


const LoginPage = () => {
    const {register, handleSubmit} = useForm<LoginCreadentials>()

    const loginUser = (data: LoginCreadentials) => {
        try{
            const response = AxiosRequest.post('/token', {
                username: data.username,
                password: data.password
            })
            console.log('Вход успешный', response)
        }catch(e){
            console.error(e)
        }
    }
    return(
        <>
        <form onSubmit={handleSubmit(loginUser)}>
            <input type="text" {...register('username')}/>
            <input type="text" {...register('password')}/>
            <button type='submit'>логин</button>
        </form>
        </>
    )
}

export default LoginPage