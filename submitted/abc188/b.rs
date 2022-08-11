use proconio::input;

fn main() {
    input! {
        n: usize,
        a:[i64; n],
        b:[i64; n],
    }
    let mut val = 0;
    for i in 0..n {
        val += a[i] * b[i]
    }
    if val == 0 {
        println!("Yes")
    } else {
        println!("No")
    }
}