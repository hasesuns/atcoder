use proconio::input;
use proconio::marker::Chars;
use std::collections::HashMap;

fn main() {
    input! {
        s: Chars
    }
    let mut has_num_counter: HashMap<&char, i32> = HashMap::new();
    s.iter().for_each(|ss| {
        let count = has_num_counter.entry(&ss).or_insert(0);
        *count += 1;
    });

    if s.len() == 1 {
        if s[0] as i32 - 48 == 8 {
            println!("Yes");
        } else {
            println!("No");
        }
        return;
    }
    if s.len() == 2 {
        let s0 = s[0] as i32 - 48;
        let s1 = s[1] as i32 - 48;
        if (s0 * 10 + s1) % 8 == 0 || (s1 * 10 + s0) % 8 == 0 {
            println!("Yes");
        } else {
            println!("No");
        }
        return;
    }

    let mut check_num = 104; // minimum "multiple of 8, bigger than 99"
    'outer: loop {
        if check_num == 1000 {
            break;
        }
        let check_num_str = check_num.to_string();
        let check_num_chars: Vec<char> = check_num_str.chars().collect();
        let mut need_num_counter: HashMap<&char, i32> = HashMap::new();
        check_num_chars.iter().for_each(|c| {
            let count = need_num_counter.entry(c).or_insert(0);
            *count += 1;
        });
        check_num += 8;
        for (key, need_cnt) in need_num_counter.iter() {
            match has_num_counter.get(key) {
                Some(has_cnt) => {
                    if has_cnt < need_cnt {
                        continue 'outer;
                    }
                }
                None => {
                    continue 'outer;
                }
            }
        }
        println!("Yes");
        return;
    }
    println!("No");
}