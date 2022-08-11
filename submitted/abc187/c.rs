use proconio::input;
use std::collections::HashSet;

fn main() {
    input! {
        n: usize,
        s: [String; n]
    }
    let mut s0 = HashSet::new();
    let mut s1 = HashSet::new();
    for i in 0..n {
        if s[i].chars().nth(0).unwrap() == '!' {
            s1.insert(s[i][1..].to_string());
        } else {
            s0.insert(s[i].to_string());
        }
    }
    for ss0 in &s0 {
        if s1.contains(ss0) {
            println!("{}", ss0);
            return;
        }
    }
    println!("satisfiable")
}