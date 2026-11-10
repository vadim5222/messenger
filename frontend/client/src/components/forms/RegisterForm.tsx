import { useForm } from "react-hook-form"
import AxiosRequest from "../../utils/AxiosRequest"
import type RegisterCredentials from "../../interfeces/RegisterCredentials"



const RegisterForm = ({onSuccess}: {onSuccess: () => void}) => {

    const {register, handleSubmit} = useForm<RegisterCredentials>()

    const registerUser = async (data: RegisterCredentials) => {
        try{
            const response = await AxiosRequest.post('/register', {
                name: data.name,
                surname: data.surname,
                username: data.username,
                age: data.age,
                password: data.password,
            }, {
                headers: {
                    'Content-Type':'application/json'
                }
            })
            console.log('Регистрация прошла успешно', response)
            if (response) {
                onSuccess()
            }
        }catch(e){
            console.error(e)
        }
    }



    return(
        <>
        <form onSubmit={handleSubmit(registerUser)}>
            <input type="text" {...register('name')}/>
            <input type="text" {...register('surname')}/>
            <input type="text" {...register('username')}/>
            <input type="number" {...register('age')}/>
            <input type="password" {...register('password')}/>
            <button>Зарегистрироваться</button>
        </form>
        </>
    )
}

export default RegisterForm