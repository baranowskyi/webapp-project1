export function validateEmail(email) {                        
        if (email != '' &&  (/^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/i.test(email))) {                
            return true
        }            
    }

export function validatePassword(password) {
        if (password != '' && (/^[A-Za-z0-9-_!@#$%^&*?]{4,30}$/i.test(password))) {
            return true
        }
    }    

