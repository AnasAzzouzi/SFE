import React,{Component} from 'react'

import {Button, Form, FormGroup} from 'react-bootstrap'
import axios from 'axios'

class PasswordChange extends Component{

state={

    recruiter:{}
}
    async componentWillReceiveProps({recruiter}){
        await this.setState({recruiter:recruiter})
        console.log(this.state)
    }
    async onFormSubmit(e){
        
        e.preventDefault()
        var oldPass=document.getElementById('Opw').value
        var NewPass=document.getElementById('Npw').value
        var ConfNpw=document.getElementById('ConfNpw').value
        if (oldPass!==this.state.recruiter.Password){
            document.getElementById('Error').innerHTML="Old Password isn't Correct"

        }else if(NewPass!==ConfNpw){
            document.getElementById('Error').innerHTML="The Two Passwords aren't identical"
        }
        else{
            const recruiter = { ...this.state.recruiter }
            recruiter.Password=NewPass
            await this.setState(() => ({ recruiter }))
            console.log(this.state.recruiter)
            axios.post('http://127.0.0.1:8000/career/Updaterecruiter',this.state.recruiter).then(res=>console.log(res.data)).then(()=>window.location.reload(false))

        }
    }
    render(){


        return(
            <div onSubmit={(e)=>this.onFormSubmit(e)}>
                <Form>  <FormGroup >
                            <Form.Control type="Password" id="Opw" name="OldPassword" /*onChange ={(e)=>this.onTextChange(e)} */name="OldPassword" placeholder="Old Password" required/>
                        </FormGroup>
                        
                        <FormGroup >
                            <Form.Control type="password" id="Npw" name="NewPassword" placeholder="New Your Password" required/>
                        </FormGroup>
                        <FormGroup >
                            <Form.Control type="password" id="ConfNpw" placeholder="Confirm New Your Password" required/>
                        </FormGroup>
                        <p id="Error"> </p>
                        <Button type="submit">Change</Button>
                </Form>
                      
            </div>
        );
    }

}
export default PasswordChange