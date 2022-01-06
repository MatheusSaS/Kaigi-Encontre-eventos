import { http } from './config'

export default{    
    register: (user) =>{
        return http.post('register',user)
    },
    login: (email,pass) =>{
        return http.get('login',{auth:{username:email,password:pass}})
    },    
    user: (public_id) =>{                
        return http.get('user/'+public_id)
    },
    alteruser: (public_id,user) =>{                
        return http.put('user/'+public_id,user)
    }
}