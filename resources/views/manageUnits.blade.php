@extends('layouts.app')



@section('content')
    <div class="container">
        <div class="row">
            <div class="col-md-10 col-md-offset-1">
                <div class="w3-container w3-center">
                    <h1>Basic Unit Information</h1>
                </div>

                <span class="w3-tag w3-small w3-theme-d5">Unit Name/Number: {{$building->name}}</span>
                <br>
                <span class="w3-tag w3-small w3-theme-d5">Tenant: {{$building->address}}</span>
                <br>
                <span class="w3-tag w3-small w3-theme-d5">Property Owner: {{$building->owner}}</span>
                <br>
                {{--
                the below code is trash. need to remove
               --}}


            </div>
        </div>
    </div>
@endsection