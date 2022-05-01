#[macro_use] extern crate rocket;

#[get("/")]
fn index() -> &'static str {
    "I am an insecure HTTP server pls secure me OwO"
}

#[launch]
fn rocket() -> _ {
    rocket::build().mount("/", routes![index])
}
