use proconio::input;

fn main() {
    input! {
        a: i32,
        b: i32
    }
    let sa = a.to_string().chars().fold(0, |sum, x| sum + x as i32 - 48);
    let sb = b.to_string().chars().fold(0, |sum, x| sum + x as i32 - 48);
    if sa >= sb {
        println!("{}", sa)
    } else {
        println!("{}", sb)
    }
}