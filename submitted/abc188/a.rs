use proconio::input;
fn main() {
    input! {
        xy: (i64, i64)
    }
    let diff = (xy.0 -xy.1).abs();
    if diff < 3 {
        println!("Yes")
    } else {
        println!("No")
    }
}