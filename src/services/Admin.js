import { http } from './config'

export default{    
    createSubject: (subject) =>{
        return http.post('admin/subject',subject)
    },
    alterSubjects: (public_id,subject) =>{
        return http.put('admin/subject/'+public_id,subject)
    },
    deleteSubjects: (public_id) =>{
        return http.delete('admin/subject/'+public_id)
    },
    subjects: () =>{
        return http.get('admin/subject')
    },   
    
    createCategory: (Category) =>{
        return http.post('admin/category',Category)
    },
    alterCategory: (public_id,Category) =>{
        return http.put('admin/category/'+public_id,Category)
    },
    deleteCategory: (public_id) =>{
        return http.delete('admin/category/'+public_id)
    },
    category: () =>{
        return http.get('category')
    },     
}