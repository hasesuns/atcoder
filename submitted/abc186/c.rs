use proconio::input;

fn main() {
    input! {
        n: usize
    }
    let mut ans = 0;
    for i in 1..=n {
        if format!("{}", i).find('7').is_none() && format!("{:o}", i).find('7').is_none() {
            ans += 1
        }
    }
    println!("{}", ans)
}