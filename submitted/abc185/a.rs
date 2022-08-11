use proconio::input;

fn main() {
    input! {
        a: [usize; 4]
    }
    let ans = a.iter().min().unwrap();
    println!("{}", ans);
}