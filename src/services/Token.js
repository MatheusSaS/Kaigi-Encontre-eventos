import { http } from './config'

export default{    
    setToken: () =>{
        try {
            http.defaults.headers.common['x-access-token'] = localStorage.getItem('token')
            return true
        } catch (error) {
            return {'error':error}
        }        
    },
    CheckAuth: () =>{
        if(localStorage.getItem('token')){
            return true
        } else{
            return false
        }
    }
}